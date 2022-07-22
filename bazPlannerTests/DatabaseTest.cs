namespace bazPlannerTests
{
    [TestClass]
    public class DatabaseTest
    {
        [TestMethod]
        public void ConnectTest()
        {
            string nameDatabase = "qwerty.db";
            string expected = "test.db";
            
            bazPlanner.Models.Database.Connect(nameDatabase);

            Assert.AreEqual(expected, nameDatabase);
        }

        [TestMethod]
        public void ConnectTest2()
        {
            string nameDatabase = "test.db";
            string expected = "test.db";

            bazPlanner.Models.Database.Connect(nameDatabase);

            Assert.AreEqual(expected, nameDatabase);
        }
    }
}