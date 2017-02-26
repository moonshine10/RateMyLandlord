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
    <title>Rate my Landlord</title>
      <c:url value="/static/bower_components/bootstrap/dist/css/bootstrap.css" var="bootstrapcss"></c:url>
      <c:url value="/static/bundles/local/bundle.js" var="bundle"></c:url>
      <c:url value="/static/bundles/local/vendors.js" var="vendors"></c:url>
      <c:url value="/static/css/index.css" var="css"></c:url>
      <link rel="stylesheet" href="${bootstrapcss}" />
      <link rel="stylesheet" href="${css}">
  </head>
  <body>
  <div id="maincontainer">

  </div>
  <script src="${vendors}"></script>
  <script src="${bundle}"></script>

  </body>
</html>
