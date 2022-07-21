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
    }
}
