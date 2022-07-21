using System.Diagnostics;
using System.Windows;
using bazPlanner.Models;

namespace bazPlanner.Forms
{
    public partial class AddTask : Window
    {
        //Add new task.
        public AddTask()
        {
            InitializeComponent();
            //Add items to ComboBox from Database table.
            for(int i = 0; i < 3; i++)
            {
                comboPriority.Items.Add(Database.SelectPriority()[i]);
            }     
        }

        //Add new task in table of database.
        private void AddNewTask(object sender, RoutedEventArgs e)
        {
            string ProjectID = Database.SelectOwner(((MainWindow)Application.Current.MainWindow).labelAuth.Content.ToString());
            Database.InsertTask(textNameTask.Text, ProjectID, comboPriority.Text.ToString(), dateTaskStart.Text.ToString(), dateTaskEnd.Text.ToString());
        }
    }
}
