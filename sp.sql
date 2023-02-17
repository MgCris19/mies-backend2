DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `accionesMenu`(IN perfil INT, IN pantalla int)
BEGIN
	select ac.nombre from tbl_accion  ac
	inner join tbl_perfil_has_pantalla_has_accion ph on ph.id_accion = ac.id_accion
	where ph.id_perfil = perfil and ph.id_pantalla = pantalla and ac.state = 'A'and ph.state = 'A';
END$$
DELIMITER ;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_menu_has_pantalla`(IN idMenu INT, IN idPantalla INT, IN idUser INT)
BEGIN
	DECLARE x INT DEFAULT 0;
    DECLARE s VARCHAR(1);
    
	SET x = (SELECT count(*) FROM mies_dev.tbl_menu_has_pantalla 
				WHERE  id_pantalla = idPantalla);
                
	SET s = (SELECT state FROM mies_dev.tbl_pantalla 
				WHERE id_pantalla = idPantalla);
	
	IF(x=0 and s = 'A') THEN
		INSERT INTO tbl_menu_has_pantalla (state, created_date, modified_date, id_user_created, id_menu, id_pantalla)
        VALUES ('A', NOW(),NOW(),idUser, idMenu, idPantalla);
		
        SELECT "Creación exitosa.!" message, "0" error;
	ELSE
		SELECT "Error.!" message, "1" error;
	END IF;
END$$
DELIMITER ;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_perfil_has_pantalla_has_accion`(IN idPerfil INT, IN idPantalla INT, IN idAccion INT, IN idUser INT)
BEGIN
	DECLARE x,ac INT DEFAULT 0;
    DECLARE sp, spt, sa VARCHAR(1);
    
	#SET x = (SELECT count(*) FROM mies_dev.tbl_perfil_has_pantalla_has_accion 
	#			WHERE id_accion = idAccion AND id_pantalla = idPantalla AND id_perfil = idPerfil);
	
    SET x = (SELECT count(*) FROM mies_dev.tbl_perfil_has_pantalla_has_accion 
				WHERE id_pantalla = idPantalla);
	
    SET ac = (SELECT count(*) FROM mies_dev.tbl_perfil_has_pantalla_has_accion 
				WHERE id_accion = idAccion AND id_pantalla = idPantalla);
                
	SET spt = (SELECT state FROM mies_dev.tbl_pantalla 
				WHERE id_pantalla = idPantalla);
                
	SET sp = (SELECT state FROM mies_dev.tbl_perfil 
				WHERE id_perfil = idPerfil);
	
    SET sa = (SELECT state FROM mies_dev.tbl_accion 
				WHERE id_accion = idAccion);
    
    IF(x=0 AND sp = 'A' AND spt = 'A' AND sa = 'A') THEN
		
		INSERT INTO tbl_perfil_has_pantalla_has_accion 
				(state, created_date, modified_date, id_user_created, id_accion, id_pantalla, id_perfil)
		VALUES ('A', NOW(),NOW(),idUser, idAccion, idPantalla, idPerfil);		
        
        SELECT "Creación exitosa.!" message, "0" error;
	ELSE		
		IF (ac = 0 AND x!=0 AND sp = 'A' AND spt = 'A' AND sa = 'A') THEN
			INSERT INTO tbl_perfil_has_pantalla_has_accion 
					(state, created_date, modified_date, id_user_created, id_accion, id_pantalla, id_perfil)
			VALUES ('A', NOW(),NOW(),idUser, idAccion, idPantalla, idPerfil);		
			
			SELECT "Creación exitosa.!" message, "0" error;
		ELSE
			SELECT "Error.!" message, "1" error;
		END IF;
    	
	END IF;
END$$
DELIMITER ;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_usuario_has_perfil`(IN idPerfil INT, IN idUsuario INT, IN idUser INT)
BEGIN
	DECLARE x INT DEFAULT 0;
    DECLARE s VARCHAR(1);
    
	SET x = (SELECT count(*) FROM mies_dev.tbl_usuario_has_perfil 
				WHERE id_perfil = idPerfil AND id_usuario = idUsuario);
                
	SET s = (SELECT state FROM mies_dev.tbl_perfil 
				WHERE id_perfil = idPerfil);
	
	IF(x=0 and s = 'A') THEN
		INSERT INTO tbl_usuario_has_perfil (state, created_date, modified_date, id_user_created, id_perfil, id_usuario)
        VALUES ('A', NOW(),NOW(),idUser, idPerfil, idUsuario);
		
        SELECT "Creación exitosa.!" message, "0" error;
	ELSE
		SELECT "Error.!" message, "1" error;
	END IF;
END$$
DELIMITER ;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `obtener_usuario_perfil`(IN correo VARCHAR(50), IN tipo INT)
BEGIN
	declare id int default 0;
	if (tipo = 0) then
		set id = (select id_usuario from tbl_usuario where email = correo);
	else
		set id = tipo;
	end if;
    
	select distinct perfil.id_perfil id,  perfil.nombre perfil, 
        menu.id_menu, menu.nombre menu, menu.icono, 
        pantalla.id_pantalla, pantalla.nombre pantalla,pantalla.icono,
		pantalla.uri, usuario.id_usuario
			from tbl_menu menu 
			inner join tbl_menu_has_pantalla menupant on menu.id_menu = menupant.id_menu
			and menupant.state='A'
			and menu.state='A'
			inner join tbl_pantalla pantalla on pantalla.id_pantalla = menupant.id_pantalla
			and pantalla.state='A'
			inner join tbl_perfil_has_pantalla_has_accion perf_pant_accion on perf_pant_accion.id_pantalla = pantalla.id_pantalla
			inner join tbl_perfil perfil on perfil.id_perfil = perf_pant_accion.id_perfil
			and perfil.state='A'
			inner join tbl_usuario_has_perfil user_perfil on user_perfil.id_perfil = perfil.id_perfil
			and user_perfil.state='A'
			inner join tbl_usuario usuario on usuario.id_usuario = user_perfil.id_usuario
			and usuario.state = 'A'
				where usuario.id_usuario = id
			ORDER by menu.id_menu;
END$$
DELIMITER ;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_menu_has_pantalla`(IN idMenu INT, IN idPantalla INT, IN idUser INT, IN estado VARCHAR(1))
BEGIN
	DECLARE x INT DEFAULT 0;
    DECLARE s VARCHAR(1);
    
	SET x = (SELECT count(*) FROM mies_dev.tbl_menu_has_pantalla 
				WHERE id_menu = idMenu AND id_pantalla = idPantalla);
                
	IF(x=1) THEN
		UPDATE tbl_menu_has_pantalla 
			SET state = estado,  
				modified_date = NOW(), 
				id_user_modified = idUser
			WHERE id_menu = idMenu AND
				  id_pantalla = idPantalla;      
		
        SELECT "Actualización exitosa.!" message, "0" error;
	ELSE
		SELECT "Error.!" message, "1" error;
	END IF;
END$$
DELIMITER ;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_perfil_has_pantalla_has_accion`(IN idPerfil INT, IN idPantalla INT, IN idAccion INT, IN idUser INT,IN estado VARCHAR(1))
BEGIN
	DECLARE x INT DEFAULT 0;
    DECLARE s VARCHAR(1);
    
	SET x = (SELECT count(*) FROM mies_dev.tbl_perfil_has_pantalla_has_accion 
				WHERE id_accion = idAccion AND id_pantalla = idPantalla AND id_perfil = idPerfil);
                
	IF(x=1) THEN
		UPDATE tbl_perfil_has_pantalla_has_accion 
			SET state = estado,  
				modified_date = NOW(), 
				id_user_modified = idUser
			WHERE id_accion = idAccion AND 
				  id_pantalla = idPantalla AND 
				  id_perfil = idPerfil;
		
        SELECT "Actualización exitosa.!" message, "0" error;
	ELSE
		SELECT "Error.!" message, "1" error;
	END IF;
END$$
DELIMITER ;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_usuario_has_perfil`(IN idUsuario INT, IN idPerfil INT, IN idUser INT, IN estado VARCHAR(1))
BEGIN
	DECLARE x INT DEFAULT 0;
    DECLARE s VARCHAR(1);
    
	SET x = (SELECT count(*) FROM mies_dev.tbl_usuario_has_perfil 
				WHERE id_usuario = idUsuario AND id_perfil = idPerfil);
                
	IF(x=1) THEN
		UPDATE tbl_usuario_has_perfil 
			SET state = estado,  
				modified_date = NOW(), 
				id_user_modified = idUser
			WHERE id_usuario = idUsuario AND 
				  id_perfil = idPerfil;      
		
        SELECT "Actualización exitosa.!" message, "0" error;
	ELSE
		SELECT "Error.!" message, "1" error;
	END IF;
END$$
DELIMITER ;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `verificar_accion`(IN accion VARCHAR(50), IN id INT, IN pantalla INT)
BEGIN
	DECLARE X VARCHAR(50);
    
    SET x = (select distinct u.full_name from tbl_usuario u
			inner join tbl_usuario_has_perfil up on up.id_usuario = u.id_usuario
			inner join tbl_perfil p on p.id_perfil = up.id_perfil
			inner join tbl_perfil_has_pantalla_has_accion ppa on ppa.id_perfil = p.id_perfil
			inner join tbl_pantalla pt on pt.id_pantalla = ppa.id_pantalla
			inner join tbl_accion ac on ac.id_accion = ppa.id_accion
			where pt.id_pantalla = pantalla
			and u.state = 'A'
			and p.state = 'A'
			and up.state = 'A'
			and ppa.state = 'A'
            and ac.state = 'A'
			and ac.nombre = accion);
        select x;
END$$
DELIMITER ; 
