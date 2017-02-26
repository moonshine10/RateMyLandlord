<%@ taglib prefix="c" uri="http://www.springframework.org/tags" %>
<%--
  Created by IntelliJ IDEA.
  User: saurabh
  Date: 2/25/17
  Time: 6:21 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>$Title$</title>
      <c:url value="/static/bower_components/bootstrap/dist/css/bootstrap.css" var="bootstrapcss"></c:url>
      <link rel="stylesheet" href="${bootstrapcss}" />
  </head>
  <body>
  Welcome, ${firstName}
  <input type="text" class="form-control" />
  </body>
</html>
